<?php

   include("db.php");

   session_start();

   

   if($_SERVER["REQUEST_METHOD"] == "POST") {

      // username and password sent from form 
      $myusername = mysqli_real_escape_string($conn,$_POST['username']);
      $mypassword = mysqli_real_escape_string($conn,$_POST['password']); 
      $salt = 'hello_mA1m_@_SaLT';
      $mypassword = hash('sha256', $mypassword . $salt);
      $sql = "SELECT * FROM user WHERE email = '$myusername' and password = '$mypassword'";
      $result = mysqli_query($conn,$sql);
      $count = mysqli_num_rows($result);
      if($count == 1) {		  				

         $_SESSION['login_user'] = $myusername;
         header("location: index.html");

      }else {

                             echo' <div class="alert alert-danger alert-dismissible fade show" role="alert">
                             <strong>Error!</strong> Credentials are wrong.
                             <button type="button" class="close" data-dismiss="alert" aria-label="Close"> 
                             <span aria-hidden="true">×</span> 
                             </button>
                             </div>'; 

      }

   }

?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>XPLORE DRC | Log in </title>
  <!-- Google Font: Source Sans Pro -->
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback">
  <!-- Font Awesome -->
  <link rel="stylesheet" href="plugins/fontawesome-free/css/all.min.css">
  <!-- icheck bootstrap -->
  <link rel="stylesheet" href="plugins/icheck-bootstrap/icheck-bootstrap.min.css">
  <!-- Theme style -->

  <link rel="stylesheet" href="dist/css/adminlte.min.css">

  <link rel="stylesheet" href="style1.css">
</head>

<body class="hold-transition login-page" style=" background-image: url(./dist/img/user/end2.jpeg);background-attachment: fixed;

background-repeat: no-repeat;-webkit-background-size: cover; " >

<div class="upper"  >

<div class="login-box" >
  <!-- /.login-logo -->

  <div class="card" style="border-radius: 5%; display: flex; justify-content: end;">

    <div class="card-body login-card-body " style="border-radius: 10%;" >

      <p class="login-box-msg">Sign in to start your session </p>
      <form  method="post" >

        <div class="input-group mb-3">

          <input type="email" name="username" class="form-control" placeholder="Email" required>

          <div class="input-group-append">

            <div class="input-group-text">

              <span class="fas fa-envelope"></span>

            </div>

          </div>

        </div>

        <div class="input-group mb-3">

          <input type="password" name="password" class="form-control" placeholder="Password" required>

          <div class="input-group-append">

            <div class="input-group-text">

              <span class="fas fa-lock"></span>

            </div>

          </div>

        </div>

        <div class="row">

          <div class="col-8">
          </div>

          <!-- /.col -->

          <div class="col-4">

            <button type="submit" class="btn btn-success btn-block">Sign In </button>

          </div>
		  </form>
          <!-- /.col -->

		  <br><br>

		   <div class="col-8">

            

          </div>

          <!-- /.col -->

          <div class="col-4">

            <a href="signup.php" button class="btn btn-primary btn-block">Sign Up</a>

          </div>



          

		  
        </div>



      



      <!--

	  <div class="social-auth-links text-center mb-3">

        <p>- OR -</p>

        <a href="#" class="btn btn-block btn-primary">

          <i class="fab fa-facebook mr-2"></i> Sign in using Facebook

        </a>

        <a href="#" class="btn btn-block btn-danger">

          <i class="fab fa-google-plus mr-2"></i> Sign in using Google+

        </a>

      </div>

      -->

     



      <p class="mb-1">

        <a href="password-reset-link.php">Forgot my password</a>

      </p>

  </div>



 



      

       <!-- /.social-auth-links 

      <p class="mb-0">

        <a href="register.html" class="text-center">Register a new membership</a>

      </p>

    </div>

    <!-- /.login-card-body 

  </div>

</div>

<!-- /.login-box -->



<!-- jQuery -->

<script src="plugins/jquery/jquery.min.js"></script>

<!-- Bootstrap 4 -->

<script src="plugins/bootstrap/js/bootstrap.bundle.min.js"></script>

<!-- AdminLTE App -->

<script src="dist/js/adminlte.min.js"></script>

<!-- <div >

          <img src="./portal.png" style = "width:250%; background-image: linear-gradient( to right,#6F2B76,#22346F ); margin-left:-300%;margin-top:-900px;margin-left: -300%;margin-bottom:-150%; margin-top:50px,position:relative">

        </div> -->

</body>

</html>

