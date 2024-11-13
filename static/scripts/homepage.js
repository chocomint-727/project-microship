function toggleDiv(id)
{
    console.log(id);
    var div = document.getElementById(id);
    div.style.display = div.style.display == "none" ? "block" : "none";
}

document.querySelectorAll('.option').forEach(button =>
{
    console.log(button.attributes)
    button.addEventListener('click', () =>
    {
        const isEnabled = button.getAttribute("data-enabled") === true;
        button.setAttribute("data-enabled", !isEnabled);
        button.classList.toggle("active");

        let existingInput;

        const tag = button.getAttribute("data-name");
        const type = button.getAttribute('data-type');

        try {
            existingInput = document.querySelector(`input[value=${tag}][name=${type}]`)
        } catch (error) {
            console.log("Hidden Input Tag Missing")
        }

        console.log(tag);
        console.log(existingInput);

        if (!existingInput)
        {
            console.log("Creating Hidden Input");
            let input = document.createElement('input');
            input.name = type;
            input.type = 'hidden';
            input.value = tag;
            console.log(input);
            document.getElementById('searchForm').appendChild(input);
            console.log(input);
        } else
        {
            console.log("Removing Hidden Input");
            existingInput.remove();
        }
    })
});