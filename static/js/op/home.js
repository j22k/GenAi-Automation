
    // Function to open the chat form
    function openForm() {
        const form = document.getElementById('myForm');
        form.classList.add('active'); // Add active class to show the form
    }
    
    // Function to close the chat form
    function closeForm() {
        const form = document.getElementById('myForm');
        form.classList.remove('active'); // Remove active class to hide the form
    }


// Function to display the backend response
function displayResponse(response) {
    const messageContainer = document.getElementById('chatMessages');
    const backendMessage = document.createElement('div');
    backendMessage.classList.add('chat-message', 'backend');
    backendMessage.textContent = response;

    messageContainer.appendChild(backendMessage);
    messageContainer.scrollTop = messageContainer.scrollHeight; // Scroll to the bottom
}
function handleClickOutside(event) {
    const form = document.getElementById('myForm');
    const button = document.querySelector('.open-button');
    if (form.classList.contains('active') && !form.contains(event.target) && event.target !== button) {
        closeForm();
    }
}

// Add event listener to the document to handle clicks outside
document.addEventListener('click', handleClickOutside);
// Event listener for the Enter key in the textarea
document.getElementById('msg').addEventListener('keydown', function(event) {
    if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        sendMessage();
    }
});

// Function to open a specific modal
function openModal(modalId) {
    document.getElementById(modalId).style.display = 'block';
}

// Function to close a specific modal
function closeModal(modalId) {
    document.getElementById(modalId).style.display = 'none';
}

// Add event listeners to the boxes to open the corresponding modals
document.getElementById('box1').addEventListener('click', function() {
    openModal('registrationModal');
});

document.getElementById('box2').addEventListener('click', function() {
    openModal('modal2');
});


// Close modals when clicking outside of them
window.onclick = function(event) {
    const modals = document.getElementsByClassName('custom-modal'); // Updated class name
    for (let i = 0; i < modals.length; i++) {
        if (event.target == modals[i]) {
            modals[i].style.display = 'none';
        }
    }
};


// Function to open a specific modal
function openModal(modalId) {
    document.getElementById(modalId).style.display = 'block';
}

// Function to close a specific modal
function closeModal(modalId) {
    document.getElementById(modalId).style.display = 'none';
}

// Add event listener to Box 2 to open its corresponding modal
document.getElementById('box2').addEventListener('click', function() {
    openModal('modal2');
});

// Close modals when clicking outside of them
window.onclick = function(event) {
    const modals = document.getElementsByClassName('custom-modal');
    for (let i = 0; i < modals.length; i++) {
        if (event.target == modals[i]) {
            modals[i].style.display = 'none';
        }
    }
};


// Function to open a specific modal
function openModal(modalId) {
    document.getElementById(modalId).style.display = 'block';
}

// Function to close a specific modal
function closeModal(modalId) {
    document.getElementById(modalId).style.display = 'none';
}

// Add event listener to Box 2 to open its corresponding modal
document.getElementById('box2').addEventListener('click', function() {
    openModal('modal2');
});

// Close modals when clicking outside of them
window.onclick = function(event) {
    const modals = document.getElementsByClassName('custom-modal');
    for (let i = 0; i < modals.length; i++) {
        if (event.target == modals[i]) {
            modals[i].style.display = 'none';
        }
    }
};


// Function to open a specific modal
function openModal(modalId) {
    document.getElementById(modalId).style.display = 'block';
}

// Function to close a specific modal
function closeModal(modalId) {
    document.getElementById(modalId).style.display = 'none';
}



// Close modals when clicking outside of them
window.onclick = function(event) {
    const modals = document.getElementsByClassName('custom-modal');
    for (let i = 0; i < modals.length; i++) {
        if (event.target == modals[i]) {
            modals[i].style.display = 'none';
        }
    }
};


// Function to open the patient registration modal
function openPatientRegistrationModal() {
    var modal = document.getElementById('modal2');
    modal.style.display = 'block';
}

// Function to close the patient registration modal
function closePatientRegistrationModal() {
    var modal = document.getElementById('modal2');
    modal.style.display = 'none';
}

// Close the modal if the user clicks outside of it
window.onclick = function(event) {
    var modal = document.getElementById('modal2');
    if (event.target === modal) {
        closePatientRegistrationModal();
    }
};
// Function to open the patient registration modal
function openPatientRegistrationModal() {
    var modal = document.getElementById('modal2');
    modal.style.display = 'block';
}

// Function to close the patient registration modal
function closePatientRegistrationModal() {
    var modal = document.getElementById('modal2');
    modal.style.display = 'none';
}

// Close the modal if the user clicks outside of it
window.addEventListener('click', function(event) {
    var modal = document.getElementById('modal2');
    var modalContent = document.querySelector('.custom-modal-content');

    if (event.target === modal && !modalContent.contains(event.target)) {
        closePatientRegistrationModal();
    }
});
function copyTokenNumber() {
    // Get the input element
    var tokenInput = document.getElementById('tokenNumber');
    
    // Select the text inside the input field
    tokenInput.select();
    tokenInput.setSelectionRange(0, 99999); // For mobile devices
    
    // Copy the text inside the input field
    document.execCommand('copy');
    
    // Optionally, provide feedback
    alert('Token number copied to clipboard!');
}
document.getElementById('patientRegistrationForm').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent form submission

    const formData = new FormData(this);
    const data = Object.fromEntries(formData.entries());

    fetch('/op/patient_registration', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.status) {
            const tokenInput = document.getElementById('tokenNumber');
            tokenInput.value = data.user_id;
            alert(data.message);
        } else {
            showAlert('danger-alert', data.message);
        }
    })
    .catch((error) => {
        showAlert('danger-alert', error);
    });

    return false; // Ensure the form doesn't reload the page
});


// Example usage: openPatientRegistrationModal();

// Example usage: openPatientRegistrationModal();

// Function to send a message
function sendMessage() {
    const messageContainer = document.getElementById('chatMessages');
    const messageInput = document.getElementById('msg');
    const message = messageInput.value;

    if (message.trim() !== "") {
        // Display the user message
        const userMessage = document.createElement('div');
        userMessage.classList.add('chat-message', 'user');
        userMessage.textContent = message;
        messageContainer.appendChild(userMessage);
        messageInput.value = '';
        messageContainer.scrollTop = messageContainer.scrollHeight; // Scroll to the bottom

        // Send the message to the backend
        fetch('/send_message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ msg: message }),
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            displayResponse(data.response_message);
            
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }
}

function showAlert(alertId, message) {
    const alertElement = document.getElementById(alertId);
    alertElement.innerText = message;
    alertElement.style.display = 'block';

    // Automatically hide the alert after 5 seconds (optional)
    setTimeout(() => {
        alertElement.style.display = 'none';
    }, 5000);
}