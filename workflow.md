Workflow
========

Committing User
---------------
  
  	Login
     Spotify Auth
       Reject
         try Again         
    
    Get Playlists
      Search For "Anon"
        If not found - Inform User and give instructions
        
        If found - Display to Commiting User
          Progress with Commit
             No - Do Nothing
             Yes - Send to Tape Library - Write Spotify URL to DB


Listening User
---------------
 	 Login
     Spotify Auth
       Reject
         try Again 
         
   	 Check on Web site for new Tapes
      If not found - Display Message
      If found - Resond with Spotify URLKPrompt Listening User to listen to tape
        No - Do Nothing
        Yes - Load play list
          Anonmise
          Play
        
        
            
        
