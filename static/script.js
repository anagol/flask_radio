function get_track() {
    const station = ['Belarus', 'Ukraine', 'Humor']
    station.forEach(stat => {
        // console.log(stat)
        fetch(`/track?station=${stat}`).then(r => r.json()).then(data => {
            const tr = document.querySelector(`#${stat} .track`)
            // console.log(tr)
            tr.innerText = data.track
            console.log(data)
        })
    })
}

setInterval(get_track, 3000)