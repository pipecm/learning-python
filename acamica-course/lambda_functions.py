say_hello = lambda: "Hello world"
greet = lambda name: "Hello {}, welcome home!".format(name)
re_greet = lambda name, surname: "Hello {} {}, welcome home!".format(name, surname)
get_avg = lambda marks: sum(marks)/len(marks) if marks else 0.0

output_list = [say_hello(), greet("Jack"), re_greet("John", "Jackson")]
for output in output_list:
    print(output)

print(str(get_avg([5.0, 6.0, 7.0])))
print(str(get_avg([])))