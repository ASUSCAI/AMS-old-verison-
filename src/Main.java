import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.RandomAccessFile;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class Main {

    private static CardReader reader;

    public static void main(String[] args) {
        Statement statement = sqlInit();
        reader = new CardReader(statement, "ART220");
        try (BufferedReader in = new BufferedReader(new InputStreamReader(System.in))) {
            reader.startMonitor(in);
        } catch (IOException|SQLException|InterruptedException e) {
            e.printStackTrace();
            // TODO: make this restart?
            // reader.startMonitor(in);
        }
    }

    private static Statement sqlInit() {
        Connection connection = null;
        try {
            // create a database connection
            connection = DriverManager.getConnection("jdbc:sqlite:sample.db");
            Statement statement = connection.createStatement();
            statement.setQueryTimeout(30); // set timeout to 30 sec.

            // * just for testing, recreate table every time
            // statement.executeUpdate("DROP TABLE IF EXISTS KeycardScans");
            statement.executeUpdate("CREATE TABLE KeycardScans (time INTEGER, room TEXT, sid INTEGER, inOut INTEGER)");
            // ResultSet rs = statement.executeQuery("SELECT * FROM KeycardScans");
            // while (rs.next()) {
            //     // read the result set
            //     System.out.println("name: " + rs.getString("name"));
            //     System.out.println("id: " + rs.getInt("id"));
            // }
            return statement;
            // return connection;
        } catch (SQLException e) {
            // if the error message is "out of memory",
            // it probably means no database file is found
            System.err.println(e.getMessage());
        } finally {
            // try {
            //     if (connection != null)
            //         connection.close();
            // } catch (SQLException e) {
            //     // connection close failed.
            //     System.err.println(e.getMessage());
            // }
        }
        return null;
    }
}