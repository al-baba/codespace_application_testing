# Setting Up
<br>

## Conda Environment 
<br>

### Reinstall packages from an export file 

<pre><code> $ conda env create --name <your_env_name> --file FILE </code></pre>


<br>

### Install with requirements.txt and pip into conda environment
First create empty conda env
 

  
<pre><code>  $ conda create -n <my_env>
  $ source activate base 
  $ conda acivate <my_env>
</code></pre>




[...instead of just calling pip install <package>, you can use the module flag -m with python so that it uses the anaconda python for the installation](https://stackoverflow.com/a/56889729/14327910)


<pre><code> $ python -m pip install -r requirements.txt </code></pre>

