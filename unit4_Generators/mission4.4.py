# To finish
def gen_secs():
    i = 0
    while i < 60:
        print(i)
        yield i
        i += 1


def gen_minutes():
    for i in range(0, 60):
        yield i


def gen_hours():
    i = 0
    while i < 24:
        yield i
        i += 1


def gen_time():
    for i in range(0, 24):
        for j in range(0, 60):
            for k in range(0, 60):
                generator_hour = gen_hours()
                generator_minute = gen_minutes()
                generator_sec = gen_secs()
                hour = next(generator_hour)
                minute = next(generator_minute)
                sec = next(generator_sec)
                print(hour)
                yield "%02d:%02d:%02d" % (hour, minute, sec)


for gt in gen_time():
    print(gt)

gt_hour = gen_time()

print(next(gt_hour))
print(next(gt_hour))
print(next(gt_hour))
