function deleteNote(noteId) {
    // Send post request to this endpoint
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({ noteId: noteId })
        // When it gets a response from that endpoint, reload
        // the window on the homepage
    }).then((_res) => {
        window.location.href = "/";
    });
}