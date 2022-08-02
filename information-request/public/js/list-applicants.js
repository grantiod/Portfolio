async function getAllApplicants() {
    const response = await fetch('/api/applicants');
    const data = await response.json();

    const tableContent = document.getElementById('table-content');

    for (const applicant of data) {
        tableContent.innerHTML += `
            <tr>
                <td>${applicant.fname}</td>
                <td>${applicant.lname}</td>
                <td>${applicant.email}</td>
                <td>${applicant.phone}</td>
                <td>${applicant.campus}</td>
                <td>${applicant.request}</td>
                <td>${applicant.dateOfApplication}</td>
                <td><input type="checkbox" id="requestComplete" value="complete"></td>
            </tr>
        `
    }
}