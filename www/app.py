# logging模块定义了一些函数和模块，可以帮助我们对一个应用程序或库实现一个灵活的事件日志处理系统
# logging模块可以纪录错误信息，并在错误信息记录完后继续执行
# 设置logging的默认level为INFO
# 日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
import logging
logging.basicConfig(level=logging.INFO)
# asyncio 内置了对异步IO的支持
import asyncio 
# os模块提供了调用操作系统的接口函数
import os
# json模块提供了Python对象到Json模块的转换
import json
# time模块提供各种操作时间的函数
import time
# datetime是处理日期和时间的标准库
from datetime import datetime
# aiohttp是基于asyncio实现的http框架
from aiohttp import web


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>')

# 调用asyncio实现异步IO
async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

# asyncio的编程模块实际上就是一个消息循环。我们从asyncio模块中直接获取一个eventloop（事件循环）的引用，//
# 然后把需要执行的协程扔到eventloop中执行，就实现了异步IO
# 第一步是获取eventloop

# get_event_loop() => 获取当前脚本下的事件循环，返回一个event loop对象(这个对象的类型是'asyncio.windows_events._WindowsSelectorEventLoop')，\
#   实现AbstractEventLoop（事件循环的基类）接口
# 如果当前脚本下没有事件循环，将抛出异常，get_event_loop()永远不会抛出None
loop = asyncio.get_event_loop()
# 之后是执行curoutine
loop.run_until_complete(init(loop))
# 无限循环运行直到stop()
loop.run_forever()