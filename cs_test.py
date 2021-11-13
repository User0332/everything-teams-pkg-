import System;
from System import Console;
from System.Threading import Thread;


class CSharpProgram:
	class MyFirstProgram:
		def Main(*args):
			Console.WriteLine("Hello World!");
			Console.WriteLine("What is your name?");
			Thread.Sleep(2000);
			name = Console.ReadLine();
			Thread.Sleep(2000);
			Console.WriteLine(f"Hello, {name}!");
			Thread.Sleep(500);
			Console.WriteLine("Goodbye!");
			Thread.Sleep(1000);
			Console.WriteLine(f"Args: {args}");


if __name__ == "__main__":
	CSharpProgram.MyFirstProgram.Main(*System.args);