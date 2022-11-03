$(document).ready(function () {
    $(".household_income").on("change",function () {
        search_term = $(this).val();
        $('#household-table tbody tr').each(function () {
            var sel = $(this);
            var txt = sel.find('td:eq(13)').text();
            if (search_term !='All') {
                if (txt.indexOf(search_term) === -1) {
                    $(this).hide();
                }
                else {
                    $(this).show();
                }
            }
            else
            {
                $('#household-table tbody tr').show();
            }
        });
    });
});