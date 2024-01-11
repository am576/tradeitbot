function createDivRow(itemName, price) {
  let row = document.createElement('div');
  row.classList.add('row-container','item-row');

  let nameLabel = document.createElement('div');
  nameLabel.classList.add('item-name', 'col-6');
  nameLabel.textContent =  itemName;
  row.appendChild(nameLabel);

  let priceLabel = document.createElement('div');
  priceLabel.classList.add('item-price','col-4');
  priceLabel.textContent =  price;
  row.appendChild(priceLabel);

  let buttonsContainer = document.createElement('div');
  buttonsContainer.classList.add('buttons-container','col-2');
  row.appendChild(buttonsContainer);

  let editButton = document.createElement('button');
  editButton.classList.add('btn', 'btn-primary', 'btn-sm', 'edit-button');
  editButton.innerHTML = '<span class="mdi mdi-pencil"></span>';
  editButton.addEventListener('click',
      function() {
          editButton.style.display = 'none';
          nameLabel.style.display = 'none';
          priceLabel.style.display = 'none';

          let nameInput = document.createElement('input');
          nameInput.classList.add('name-input')
          nameInput.type = 'text';
          nameInput.value = itemName;
          nameInput.addEventListener("keypress", function(event) {
              if (event.key === "Enter") {
                  hideInputs()
              }
          });
          row.insertBefore(nameInput, buttonsContainer);

          let priceInput = document.createElement('input');
          priceInput.classList.add('price-input')
          priceInput.type = 'text';
          priceInput.value = price;
          priceInput.addEventListener("keypress", function(event) {
              if (event.key === "Enter") {
                  hideInputs()
              }
          });
          row.insertBefore(priceInput, buttonsContainer);

          row.setAttribute("editing", true)
      });
  buttonsContainer.appendChild(editButton);

  var deleteButton = document.createElement('button');
  deleteButton.classList.add('btn', 'btn-danger', 'btn-sm');
  deleteButton.innerHTML = '<span class="mdi mdi-trash-can-outline"></span>';
  deleteButton.addEventListener('click', function() {
      $('#confirm-modal').modal('show');
      $('#confirm-remove').off('click').on('click', function() {
          row.remove();
          $('#confirm-modal').modal('hide');
      });
  });
  buttonsContainer.appendChild(deleteButton);
  
  return row;
}

function handleClickOutsideInputs(event) {
  let input1s = document.querySelectorAll(".name-input");
  let input2s = document.querySelectorAll(".price-input");
  let editButtons = document.querySelectorAll(".edit-button");

  var isInsideInputs = Array.from(input1s).some(function (input1) {
      return input1.contains(event.target);
  }) || Array.from(input2s).some(function (input2) {
      return input2.contains(event.target);
  });

  var isInsideEditButtons = Array.from(editButtons).some(function (editButton) {
      return editButton.contains(event.target);
  });

  if (!isInsideInputs && !isInsideEditButtons) {
      hideInputs();
  }
}   
function hideInputs() {
  const rows = document.getElementsByClassName("item-row");
  Array.from(rows).forEach(function(row) {
      var isEditing = row.getAttribute("editing") === "true";
      if (isEditing) {
          const nameLabel = row.querySelector('.item-name');
          const nameInput = row.querySelector('.name-input');
          const priceLabel = row.querySelector('.item-price');
          const priceInput = row.querySelector('.price-input');
          const editButton = row.querySelector('.edit-button');
          editButton.style.display = 'block';
          nameLabel.style.display = 'block';
          nameLabel.textContent = '' + nameInput.value;
          nameInput.remove();
          priceLabel.style.display = 'block';
          priceLabel.textContent = '' + priceInput.value;
          priceInput.remove();
          row.setAttribute("editing", false)
      }
  });
}

function saveItems() {
  const rows = document.getElementsByClassName("item-row");
  let items = [];
  for (let row of rows) {
    const name = row.children[0].innerHTML
    const price = row.children[1].innerHTML
    items.push({name: name, price: price});
  }
  console.log(items);
  eel.saveItems(items);
}