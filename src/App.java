import java.io.IOException;
import java.io.RandomAccessFile;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import org.python.util.PythonInterpreter;

public class App {

    private static int count = 3;

    public static void main(String[] args) {
        Statement statement = sqlTest();
        try {
            cardReadTest(statement);
        } catch (IOException | InterruptedException | SQLException e) {
            e.printStackTrace();
        }
        jythonTest();
    }

    private static void cardReadTest(Statement statement) throws IOException, InterruptedException, SQLException {
        RandomAccessFile in = new RandomAccessFile("ids.txt", "r");
        String line;
        while (true) {
            if ((line = in.readLine()) != null && line.length() > 0) {
                System.out.println(line.trim());
                statement.executeUpdate("INSERT INTO Students VALUES(" + count++ + ", 'John Doe')");
                // TODO: pull student name and other data from a mock PeopleSoft database
            } else {
                Thread.sleep(2000); // check file every 2 sec
            }
        }
    }

    private static void jythonTest() {
        try (PythonInterpreter pyInterp = new PythonInterpreter()) {
            // pyInterp.exec("from canvasapi import Canvas");
            pyInterp.exec("print('Hello Python World!')");
        }
    }

    private static Statement sqlTest() {
        Connection connection = null;
        try {
            // create a database connection
            connection = DriverManager.getConnection("jdbc:sqlite:sample.db");
            Statement statement = connection.createStatement();
            statement.setQueryTimeout(30); // set timeout to 30 sec.

            statement.executeUpdate("DROP TABLE IF EXISTS Students");
            statement.executeUpdate("CREATE TABLE Students (id INTEGER, name TEXT)");
            statement.executeUpdate("INSERT INTO Students VALUES(1, 'John Doe')");
            statement.executeUpdate("INSERT INTO Students VALUES(2, 'Bob Good')");
            ResultSet rs = statement.executeQuery("SELECT * FROM Students");
            while (rs.next()) {
                // read the result set
                System.out.println("name: " + rs.getString("name"));
                System.out.println("id: " + rs.getInt("id"));
            }
            return statement;
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