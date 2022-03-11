public class Stack {
    class Node {  
        int item; 
        Node next;  
   
        public Node(int item) {  
            this.item = item;  
        }  
    }

    private int size = 0;
    private Node top;

    public int peek() {
        return top.item;
    }

    public void push(int x) {
        Node n = new Node(x);
        n.next = top;
        top = n;
        size++;
    }

    public void pop() {
        if (size == 0)
            return;
        
        top.next = top;
        size--;
    }

    public void print() {
        Stack s = new Stack();
        while (top != null) {
            System.out.print(top.item + " ");
            s.push(top.item);
            pop();
        }
        while (s.top() != null) {
            push(s.peek());
            s.pop();
        }
    }

    private Node top() {
        return top;
    }
}