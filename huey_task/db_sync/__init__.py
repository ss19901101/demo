from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('mysql+pymysql://root:19901101@localhost:3306/demo', echo=True,
                       max_overflow=0,  # 超过连接池大小外最多创建的连接
                       pool_size=5,  # 连接池大小
                       pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
                       pool_recycle=-1)  # 多久之后对线程池中的线程进行一次连接的回收（重置）
Base = declarative_base()

SessionFactory = sessionmaker(bind=engine,
                              autocommit=True)

sa = scoped_session(SessionFactory)
