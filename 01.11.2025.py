# import
# from
# from
#
# p1=Process(target=cpu_b, args=(count,))
# p2=Process(target=cpu_b, args=(count,))
# p1.start()
# p2.start()

import asyncio

async def f1():
    print("f2 boshlandi")
    await asyncio.sleep(3)
    print("f3 tugadi")

async def f3():
    await asyncio.gather(f1(),f2())

asyncio.run(f3())
def f01():
    print("f01 boshlandi")
    time.sleep(5)
    print("f01 tugadi")