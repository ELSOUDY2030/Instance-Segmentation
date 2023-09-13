# Instance-Segmentation
Instance Segmentation Tooth Dentistry

<div align="center">
    <img id="image1" src="https://github.com/ELSOUDY2030/Instance-Segmentation/blob/main/img/img1.jpg">
    <img id="image2" src="https://github.com/ELSOUDY2030/Instance-Segmentation/blob/main/img/img2.png" style="display: none;">
</div>

<script>
    var currentImage = 1;

    function toggleImage() {
        var image1 = document.getElementById('image1');
        var image2 = document.getElementById('image2');

        if (currentImage === 1) {
            image1.style.display = 'none';
            image2.style.display = 'block';
            currentImage = 2;
        } else {
            image1.style.display = 'block';
            image2.style.display = 'none';
            currentImage = 1;
        }
    }

    // تعيين التبديل التلقائي كل 5 ثوانٍ (يمكنك تغيير الفاصل الزمني حسب رغبتك)
    setInterval(toggleImage, 5000); // 5000 مللي ثانية تعني 5 ثوانٍ
</script>

