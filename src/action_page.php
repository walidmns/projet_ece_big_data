<?php 
	$productlink = $_POST["search"];
	$url = "http://localhost:8000/amazonbestprice?url=$productlink" ;
	//echo($url);
	$json = file_get_contents($url);
	#var_dump(json_decode($json));
	#var_dump(json_decode($json, true));
	//$data = json_decode($json);

	$obj = json_decode($json);
	
	$Product = $obj->{'Product'};
	
	$fr_price= $obj->{'fr'};
	$de_price= $obj->{'de'};
	$es_price= $obj->{'es'};
	$it_price= $obj->{'it'};
	$pl_price= $obj->{'pl'};
	$nl_price= $obj->{'nl'};

	$fr_link= $obj->{'link_fr'};
	$de_link= $obj->{'link_de'};
	$es_link= $obj->{'link_es'};
	$it_link= $obj->{'link_it'};
	$pl_link= $obj->{'link_pl'};
	$nl_link= $obj->{'link_nl'};

	//echo $Product->Product; //donut

	//header("Refresh:0; url=index.html");
	?>

	<!DOCTYPE html>
	<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="" />
        <meta name="author" content="" />
        <title>Amazon Dealer</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
		<link href="style.css" rel="stylesheet" />
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    </head>
    <body>
		<script>
			function goPython(){
				$.ajax({
				  url: "AmazonEU_scraper.py",
				 context: document.body
				}).done(function() {
				 alert('finished python script');;
				});
			}
		</script>
		<div class="container-fluid ">
			<div class="row justify-content-md-center">
				<div class="col-5 center-block">
					<center>
						<img src="amazon.png" alt="Amazon" width="180" height="180">
					</center>
				</div>
			</div>
			<div class="row justify-content-md-center">
				<div class="col-5 center-block" >
					<div class="search-container">
						<form action="action_page.php">
						<center>
						  <input type="text" placeholder="Amazon Product url..." name="search">
						  <button type="submit"><i class="fa fa-search"></i> Search</button>
						</center>
						</form>
					</div>
				</div>
			</div>
			<div class="row justify-content-md-center">
				
				<div class="col-1">
				</div>
				<div class="col-5 center-block">
					<table class="table table-striped center">
					  <tbody>
					  	<tr>
						  <td><?php echo $Product;?></td>
						</tr>
						<tr>
						<tr>
						  <td><img src="fr.png" alt="fr" width="25" height="20"></td>
						  <td><?php echo $fr_price;?>€</td>
						  <td><button type="action" onclick="window.open('<?php echo $fr_link;?>', '_blank')  ;" ><span class="glyphicon glyphicon-eye-open"></button></td>
						</tr>
						<tr>
						  <td><img src="de.jpg" alt="de" width="25" height="20"></td>
						  <td><?php echo $de_price;?>€</td>
						  <td><button type="action" onclick="window.open('<?php echo $de_link;?>', '_blank')  ;" ><span class="glyphicon glyphicon-eye-open"></button></td>
						</tr>
						<tr>
						  <td><img src="es.png" alt="es" width="25" height="20"></td>
						  <td><?php echo $es_price;?>€</td>
						  <td><button type="action" onclick="window.open('<?php echo $es_link;?>', '_blank')  ;" ><span class="glyphicon glyphicon-eye-open"></button></td>
						</tr>
						<tr>
						  <td><img src="it.png" alt="it" width="25" height="20"></td>
						  <td><?php echo $it_price;?>€</td>
						  <td><button type="action" onclick="window.open('<?php echo $it_link;?>', '_blank')  ;" ><span class="glyphicon glyphicon-eye-open"></button></td>
						</tr>
						<tr>
						  <td><img src="pl.png" alt="pl" width="25" height="20"></td>
						  <td><?php echo $pl_price;?>€</td>
						  <td><button type="action" onclick="window.open('<?php echo $pl_link;?>', '_blank')  ;" ><span class="glyphicon glyphicon-eye-open"></button></td>
						</tr>
						<tr>
						  <td><img src="nl.jpg" alt="nl" width="25" height="20"></td>
						  <td><?php echo $nl_price;?>€</td>
						  <td><button type="action" onclick="window.open('<?php echo $nl_link;?>', '_blank')  ;" ><span class="glyphicon glyphicon-eye-open"></button></td>
						</tr>
					  </tbody>
					</table>
				</div>
			</div>
		</div>
			
	</body>
</html>
