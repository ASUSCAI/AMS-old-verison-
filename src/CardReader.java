import java.io.IOException;
import java.io.RandomAccessFile;
import java.sql.SQLException;
import java.sql.Statement;

public class CardReader {
    private Statement statement;

    public CardReader(Statement statement) {
        this.statement = statement;
    }

    public void startMonitor(RandomAccessFile in) throws IOException, SQLException, InterruptedException {
        String line;
        while (true) {
            if ((line = in.readLine()) != null && line.length() > 0) {
                System.out.println("[LOG] READ: " + line.trim());
                String[] vals = line.split(",");
                statement.executeUpdate(
                    String.format("INSERT INTO KeycardScans VALUES(%d, %s, %d, %d)",
                    vals[0], vals[1], vals[2], vals[3])
                );
            } else {
                Thread.sleep(2000); // check file every 2 sec
            }
        }
    }
}
