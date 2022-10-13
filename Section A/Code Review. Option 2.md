Well done on attempting the problem; let’s point out some errors.

The function “reverse_mystring” (line 10), according to your documentation (comment), checks whether the string is empty or not. The method name isn’t ideal; it should reflect precisely what the method will be doing and what you wrote in the comment; in this case, it doesn’t, and that creates confusion for someone reading your code, so your documentation of the function and definition of the method doesn’t correspond with the function name; the ideal name would be something like “is_empty.”

Line 18 “return reverseString(myStr.substring(1)) + myStr.charAt(0);}” the method “reverseString” isn’t defined anywhere in your code, and this will produce an error; here you are trying to call the method “reverse_mystring” but you used a different name, that is not defined in your code, you should always mind the naming of your methods, as names or “symbols” as java tells it to you will give a compile time error since it cannot find the name or function you are calling or referring. “reverse_mystring”
2
Your method “reverse_mystring” prints “String is now empty” in line 13 and returns the string. In line 6, you store the string from this method in the variable reversed, and you print out the results in line 7, “System.out.println("The reversed string is: " + reversed + "\nFibonacci Series of 10 numbers:0 1 1 2 3 5 8 13 21 34 ");”
Remember how you defined “reverse_mystring” to check whether a string is empty? See, naming your method also caused you confusion; this goes back to the importance of naming your methods correctly. The logic in this line needs more work; first, “reverse_mystring” should do what it says, reverse the string; once that is done, the logic in line 13 will be correct, and the logic will be too (well done on this part, just this mistake needs fixing. 

Line 21, you have already defined the variable maxNumber inside the method named function and gave it a generic type of T (line 19, method parameter). You shouldn’t define and declare it again inside the method as they are in the same scope; this will throw an error in Java. I should point out that you don’t necessarily need to use generics for this problem, as you already know that your types will always be integers

You are on the right path by recursively printing the Fibonacci numbers; you need to review the logic of the things I have mentioned above.
What you can do, is change the method “reverse_mystring” so that it reverses the string and make sure it is a recursive method/function, as the question requires; make sure that the naming of your functions is consistent to avoid compile time errors, so the style of your code should be consistent, if you are using camelCase naming conversion, use that throughout your code, if you are using small letters separated by an underscore, then you have to use that conversion throughout your code.

Ideally, for Java programming, camelCase is used, and it’s popular among Java developers. 


