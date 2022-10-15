import java.io.BufferedReader;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.time.Instant;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.ZoneId;

public class CardReader {
    private Statement statement;
    private String location;

    public CardReader(Statement statement, String location) {
        this.statement = statement;
        this.location = location;
    }

    public void startMonitor(BufferedReader in) throws IOException, SQLException, InterruptedException {
        String line;
        
        ZoneId zoneId = ZoneId.systemDefault();
        LocalDate today = LocalDate.now();
        long beginning = today.atStartOfDay(zoneId).toEpochSecond();
        System.out.println("Begin: " + beginning);
        while (true) {  
            if ((line = in.readLine()) != null && line.length() > 0) {
                System.out.println("[LOG] READ: " + line.trim());
                int sid = Integer.parseInt(line.trim());

                int inOut = 1; // default 1
                // ResultSet rs = statement.executeQuery(String.format(
                //     "SELECT 1 FROM KeycardScans ORDER BY time DECE WHERE time > %d AND room=%s AND sid=%d",
                //     beginning, location, sid)
                // );
                String query = String.format(
                    "SELECT * FROM KeycardScans WHERE time > %d AND room='%s' AND sid=%d",
                    beginning, location, sid
                );
                System.out.println(query);
                ResultSet rs = statement.executeQuery(query);
                int temp = -1;
                while(rs.next()) {
                    temp = rs.getInt("inOut");
                }
                if (temp != -1) inOut = temp == 1 ? 0 : 1;

                LocalDateTime time = LocalDateTime.now();
                long epoch = time.atZone(zoneId).toEpochSecond();

                statement.executeUpdate(String.format(
                    "INSERT INTO KeycardScans VALUES(%d, '%s', %d, %d)",
                    epoch, location, sid, inOut)
                );
            } else {
                Thread.sleep(2000); // check file every 2 sec
            }
        }
    }
}
