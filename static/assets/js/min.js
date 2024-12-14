$(document).ready(function () {
    // Toggle search box visibility
    $('#search-click').click(function () {
        $('.search-box').toggle(); // يظهر أو يختفي عند الضغط
    });

    // البحث عند الضغط على زر "Enter"
    $('#form1').keypress(function (e) {
        if (e.which == 13) { // إذا تم الضغط على Enter
            let searchQuery = $('#form1').val(); // أخذ النص المدخل
            alert('بدأ البحث عن: ' + searchQuery); // يمكنك هنا استبدالها بأي عملية بحث
        }
    });
});