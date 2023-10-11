public class TorresDeHanoi {

    public static void main(String[] args) {
        torresHanoi(2, 'A', 'B', 'C');
    }

    public static void torresHanoi(int n, char origen, char intermedio, char destino) {
        if (n == 1) {
            System.out.println("DE LA " + origen + " --> " + destino + "\n");
        } else {
            torresHanoi(n - 1, origen, destino, intermedio);
            System.out.println("DE LA " + origen + " --> " + destino + "\n");
            torresHanoi(n - 1, intermedio, origen, destino);
        }
    }
}