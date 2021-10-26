from std.py import using_namespace;
#declare emptys
stdio = None;stdos = None;
stddelay = None;
Console = None;
foo = None;
exec(using_namespace('<stdio>'));
exec(using_namespace('<stddelay>'));
exec(using_namespace('<stdos>'));
exec(using_namespace('test_namespace'));



stdio.write("What is your name?\n");
name = stdio.scan();
stddelay(1000);
stdio.write(f"Hello {name}!\n");
stddelay(2000);
stdio.write(f"test_namespace.foo() on 4 and 7 = {foo(4, 7)}\n");
stdio.write('Clearing the console...\n');
stddelay(2000);
stdos.clear();
stdio.write('Console cleared. Enter any key to exit.\n');
stdio.scan();
