# 关于[RabbitMQ]的几点说明 (https://www.rabbitmq.com/)
 1. queue
 消息队列。发布者向指定消息队列发送消息，接收者进行消息消费
 依托消息队列，可以实现任务的异步执行，并且保证任务的时序性
 同时，结合exchange，可以实现消息的广播。
 > + 声明queue
 >```pythonn
 >   channel.queue_declare(queue='hello')
 >                        
 >```
 > + 发送消息
 >```pythonn
 >   channel.basic_publish(exchange='',
 >                     routing_key='hello',
 >                     body=message)
 >```
 > + 接收队列绑定
 >```pythonn
 >   channel.basic_consume(queue='hello',
 >                     auto_ack=True,
 >                     on_message_callback=callback)
 >```
 2. exchange
 类似于一种消息组的概念，一个exchange可以面向好几个queue。
 当每个queue绑定一个exchange时，即能获取到相应消息
 > + 声明exchange
 >```pythonn
 >  channel.exchange_declare(exchange='logs',
 >                        exchange_type='fanout')
 >```
 > + 发送消息
 >```pythonn
 >  channel.basic_publish(exchange='logs',
 >                     routing_key='hello',
 >                     body=message)
 >```
 > + 接收队列绑定
 >```pythonn
 >  channel.queue_bind(exchange='logs',
 >                  queue=result.method.queue)
 >```
 3. exchange_type
 针对消息组，有不同的类型
 + fanout
 以广播的形式，只要绑定exchange的queue均能收到消息
 + direct
 通过routing_key参数指定可以接收到消息的队列
 + topic
 通过形如 '*.xxx' 或者 'xxx.*' 等形式router_key去接收消息
 同时，通过#号的形式作为通配符，接收所有消息
 4. 与tornado结合
 我们使用pika作为消息中间件的连接库，该库提供了一个adapter用于使用tornado的io_loop实现异步操作
 具体使用方法见本包下的例子
 