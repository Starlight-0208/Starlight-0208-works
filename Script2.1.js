//多终端 websocket连接

//引入websocket模块
var WebSocketServer = require('websocket').server

//引入http模块 搭建http服务器
var http = require('http');

//引入时间模块
var sd = require('silly-datetime');
//时间变量
var udtime = sd.format(new Date(), 'YYYY-MM-DD HH:mm:ss');

//创建http服务器 并监听3000端口 开始监听时控制台输出文字
var server = http.createServer();
server.listen(3000,function(){
    console.log(udtime + ' [ \033[00;32m  Server  \033[00;0m ]  服务器搭建成功')
});

//储存所有终端的连接 => 数组
var cilents = [];


//创建websocket服务对象 server是个对象，通过键值对表示和创建
var wsServer = new WebSocketServer({httpServer:server});

//监听连接请求 建立连接
//websocketRequest 表示当前连接的请求
wsServer.on('request',function(websocketRequest){
    //当前连接 回话
    //websocketRequest.accept('chosen-protocol','accepted -origin') (子协议,？？？)
    var connection = websocketRequest.accept(null,'accepted-origin')

    //自加 - 连接成功
    console.log(udtime + " [\033[00;32m Connection\033[00;0m ] \033[00;32m 一个终端连接成功\033[00,0m" + ',' +"\033[00;32m 链接为：\033[00;0m" + connection.remoteAddress);
    //console.log()

    //把连接添加到终端列表 => 向数组中写入终端连接
    cilents.push(connection);

    //自加 - 连接终端数显示
    console.log(udtime + " [ \033[00;33m  System  \033[00;0m ] \033[00;33m 在线终端数：\033[00;0m" + cilents.length);

    //定时器 定时向客户端发送数据
//    setInterval(function(){
//        connection.sendUTF('hello world'+(new Date()))
//    },1000)

    //监听客户端发来的信息
    connection.on('message',function(msg){
        //当前传输的是utf8类型数据 => 判断数据类型如果是utf8类型，则解析utf8格式
        //msg.utf8Data => 解析转化为utf8数据
        if(msg.type == 'utf8'){
            //发送数据（单发）
            //connection.sendUTF(msg.utf8Data)

            //给每一个连接发送数据 => 遍历终端列表
            //forEach 即遍历
            console.log(udtime + " [ \033[00;34m  Message \033[00;0m ] \033[00;34m 客户端发送了一条消息，已转发！： \033[00;0m")
            cilents.forEach(function(item){
                //发送数据（多发）
                item.sendUTF(msg.utf8Data);
            })
        }else if(msg == "wsget.online"){
            console.log("当前有" + cilents.length + "个终端正在使用连接！")
            console.log("在线终端:");
            cilents.forEach(function(item){
                console.log(item + "is Online!");
            });
            cilents.forEach(function(item){
                item.sendUTF(msg.utf8Data);
            });
        }
    })


    //当连接断开时侯 触发的事件
    connection.on('close',function(reasonCode,description){
        console.log(udtime + ' [\033[00;32m Connection\033[00;0m ] \033[00;31m 断开了一个连接，连接为： \033[00;0m' + connection.remoteAddress);
        //获取当前索引，并根据索引在终端列表中删除对应终端
        //获取当前索引
        //index 是指定的终端（已断开） indexOf 可能是索引
        var index = cilents.indexOf(connection);
        //删除
        //index 为断开连接的终端|索引 1表示删除一个
        cilents.splice(index,1);
        //自加 - 连接终端数显示
        console.log(udtime + " [ \033[00;33m  System  \033[00;0m ] \033[00;33m 在线终端数：\033[00;0m" + cilents.length);


    })

})