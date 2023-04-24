import javax.swing.*;

public class SwingForInput {
  public static void main(String[] args) {
    String name = JOptionPane.showInputDialog("What is your name?");
    String input = JOptionPane.showInputDialog("How old are you?");
    int age = Integer.parseInt(input);
    JOptionPane.showMessageDialog(
        null, // Always use null.
        "Next year, you'll be " + (age + 1), // Message string
        "Hello, " + name, // Window caption.
        JOptionPane.INFORMATION_MESSAGE);

    System.out.println();
    System.exit(0);
  }
}
