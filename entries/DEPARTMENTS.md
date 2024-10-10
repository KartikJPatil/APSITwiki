#DEPARTMENTS


<img src="http://moodle.apsit.org.in/moodle/pluginfile.php/1/theme_essential/slide9image/1688710952/Photo_1515564165860.jpg" width="996px" height="359px" alt="dept">
## There are 4 Departments concerned with Technology
### They are:

<style>
/* Add CSS styles for the boxes */
.box {
    display: inline-block;
    width: 200px;
    height: 200px;
    border: 1px solid #ccc;
    border-radius: 10px;
    text-align: center;
    margin: 10px;
    padding: 25px;
    box-shadow: 5px 5px 5px #ccc;
    cursor: pointer;
}
.box:hover {
        background-color: #f9f9f9;
    }
/* Add CSS styles for the icons */
.icon {
    padding-top:40px;
    font-size: 48px;
    margin-bottom: 10px;
}

</style>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
<div style="display: flex;">
    <a href="/wiki/IT">
        <div class="box" onclick="animateButton(event, '/wiki/IT')">
            <i class="icon fa fa-desktop"></i>
            <p>IT</p>
        </div>
    </a>
    <a href="/wiki/deptCS">
        <div class="box" onclick="animateButton(event, '/wiki/deptCS')">
            <i class="icon fa fa-code"></i>
            <p>CS</p>
        </div>
    </a>
    <a href="/wiki/deptaiml">
        <div class="box" onclick="animateButton(event, '/wiki/deptaiml')">
            <i class="icon fa fa-cogs"></i>
            <p>AIML</p>
        </div>
    </a>
    <a href="/wiki/dscience">
        <div class="box" onclick="animateButton(event, '/wiki/dscience')">
            <i class="icon fa fa-chart-bar"></i>
            <p>DATA_SCIENCE</p>
        </div>
    </a>
</div>

<script>
function animateButton(event, redirectUrl) {
    event.preventDefault();
    const button = event.currentTarget;
    button.classList.add('animated');
    setTimeout(() => {
        button.classList.remove('animated'); // Remove the 'animated' class after the animation is complete
        window.location.href = redirectUrl;
    }, 1000);
}
</script>

<style>
.box.animated {
    animation: buttonAnimation 0.5s;
}

@keyframes buttonAnimation {
    0% {
        transform: scale(1);
    }
    50% {
        transform: scale(0.82);
    }
    100% {
        transform: scale(1);
    }
}
</style>
</div>
