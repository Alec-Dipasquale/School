//----------------------------------------------------------------------
// LinkedStringLog.java       by Dale/Joyce/Weems              Chapter 2
//
// Implements StringLogInterface using a linked list 
// of LLStringNode to hold the log strings.
//----------------------------------------------------------------------

package ch02.stringLogs;

public class LinkedStringLog implements StringLogInterface 
{
  protected LLStringNode log; // reference to first node of linked 
                              // list that holds the StringLog strings
  protected String name;      // name of this StringLog
  
  public LinkedStringLog(String name)
  // Instantiates and returns a reference to an empty StringLog object 
  // with name "name".
  {
    log = null;
    this.name = name;
  }

  public void insert(String element)
  // Precondition:   This StringLog is not full.
  //
  // Places element into this StringLog.
  {      
    LLStringNode newNode = new LLStringNode(element);
    newNode.setLink(log);
    log = newNode;
  }

  public boolean isFull()
  // Returns true if this StringLog is full, false otherwise.
  {              
    return false;
  }
  
  public int size()
  // Returns the number of Strings in this StringLog.
  {
    int count = 0;
    LLStringNode node;
    node = log;
    while (node != null)
    {
      count++;
      node = node.getLink();
    }
    return count;
  }
  
  public boolean contains(String element)
  // Returns true if element is in this StringLog,
  // otherwise returns false.
  // Ignores case difference when doing string comparison.
  {                 
    LLStringNode node;
    node = log;

    while (node != null) 
    {
      if (element.equalsIgnoreCase(node.getInfo()))  // if they match
        return true;
      else
        node = node.getLink();
    }

   return false;
  }
  
  public void clear()
  // Makes this StringLog empty.
  { 
    log = null;
  }

  public String getName()
  // Returns the name of this StringLog.
  {
    return name;
  }

  public String toString()
  // Returns a nicely formatted string representing this StringLog.
  {
    String logString = "Log: " + name + "\n\n";
    LLStringNode node;
    node = log;
    int count = 0;
    
    while (node != null)
    {
      count++;
      logString = logString + count + ". " + node.getInfo() + "\n";
      node = node.getLink();
    }
      
    return logString;
  }
  
  //new howMany operation/method by KCH

  // PRECONDITIONS: none
  public int howMany(String element)
  // Returns the number of times the string passed in element appears in the log
  // An observer operation; does not modify the ADT
  // Ignores case difference when doing string comparison
  {
    LLStringNode node;
    node = log;
    int count = 0;
    while (node != null) {
      if (element.equalsIgnoreCase(node.getInfo())) {
        count++;
      }
      node = node.getLink();
    }
  return count;
  }

  //new isEmpty() method by Alec

  //PRECONDITIONS: none
  public boolean isEmpty()
  //Returns true if Linked List is empty, false otherwise
  {
    LLStringNode node;
    node = log;
    if(node == null)
      return true;
    else
      return false;
  }

    //new uniqInsert(String element) method by Alec
    //PRECONDITIONS: none
  public boolean uniqInsert(String element)
  //Checks for element in linked list and if present returns false
  // if it is not present inserts element
  {
    LLStringNode node;
    node = log;

    while (node != null)
    {
      if (element.equalsIgnoreCase(node.getInfo()))  // if they match
        return false;
      else
        node = node.getLink();
    }
    LLStringNode newNode = new LLStringNode(element);
    newNode.setLink(log);
    log = newNode;
    return true;
  }

  //new smallest() method by Alec

  //PRECONDTIONS:String is not empty
  public String smallest()
  //returns smallest(in terms of lexicographic ordering) string in String log
  {
    LLStringNode node;
    node = log;
    String smallest = node.getInfo();
    while(node!= null)
    {
      System.out.println(node.getInfo() + ", compare to current smallest: " + node.getInfo().compareTo(smallest));
       if(node.getInfo().compareTo(smallest)<= 0){
         smallest = node.getInfo();
       }
       node = node.getLink();
    }
    return smallest;
  }
}