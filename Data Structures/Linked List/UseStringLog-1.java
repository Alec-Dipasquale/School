package main;
//----------------------------------------------------------------------------
// UseStringLog.java           by Dale/Joyce/Weems                   Chapter 2
//
// Simple example of the use of a StringLog.
//----------------------------------------------------------------------------
import ch02.stringLogs.*;

public class UseStringLog
{
  public static void main(String[] args)
  {
    StringLogInterface sample;
    sample = new LinkedStringLog("Example Use");
    sample.insert("Elvis");
    sample.insert("Elvis");
    sample.insert("Elvis");
    sample.insert("King Louis XII");
    sample.insert("Captain Kirk");
    sample.insert("Captain Kirk");

    System.out.println(sample);
    System.out.println(sample.smallest() + " is the smallest in lexicographic ordering.");
    System.out.println("\nThe size of the log is " + sample.size());
    System.out.println("Elvis shows up: " + sample.howMany("Elvis"));
    System.out.println("Trump shows up: " + sample.howMany("Trump"));
    System.out.println("Captain Kirk shows up: " + sample.howMany("Captain Kirk"));

    if(sample.isEmpty() != true)
      System.out.println("Log is not empty according to isEmpty()");

    sample.clear();
    System.out.println("Log is cleared.");

    if(sample.isEmpty() == true)
      System.out.println("Log is empty according to isEmpty()");


    sample.uniqInsert("BLACK");
    sample.uniqInsert("YELLOW");
    sample.uniqInsert("BLACK");
    sample.uniqInsert("BLACK");
    sample.uniqInsert("WHITE");
    sample.uniqInsert("BLACK");
    sample.uniqInsert("BLACK");
    sample.uniqInsert("RED");
    sample.uniqInsert("RED");
    sample.uniqInsert("WHITE");

    System.out.println(sample);

    System.out.println(sample.smallest() + " is the smallest in lexicographic ordering.");
  }
}