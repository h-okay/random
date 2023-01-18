public class ModulusAnimation {

    public static String getFrame(int frameNumber) {
        String[] frames = { ".", ".", ".", ".", ".", ".", ".", "." };
        frames[frameNumber] = "O";
        
        if (frameNumber == 0) {
            frames[7] = "o";
        } else {
            frames[frameNumber - 1] = "o";
        }

        if (frameNumber == 7) {
            frames[0] = "o";
        } else {
            frames[frameNumber + 1] = "o";
        }

        return String.join("", frames);
    }

    public static void main(String[] args) throws Exception {
        for (int i = 0; i < 80; i++) {
            System.out.print(getFrame(i % 8) + " \r");
            Thread.sleep(1000);
        }

    }
}
