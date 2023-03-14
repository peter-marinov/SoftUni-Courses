function browserHistory(browser, commands) {
    

    for (const command of commands) {
        if (command === "Clear History and Cache") {
            browser["Open Tabs"] = [];
            browser["Recently Closed"] = [];
            browser["Browser Logs"] = [];
            continue;
        }

        
        if (command.includes('Open')) {
            let tab = command.split('Open ')[1];
            browser["Open Tabs"].push(tab);
            browser["Browser Logs"].push(command);
        } else if (command.includes('Close')) { 
            let tab = command.split('Close ')[1];
            if (browser["Open Tabs"].includes(tab)) {
                let index = browser["Open Tabs"].lastIndexOf(tab);
                browser["Open Tabs"].splice(index, 1);
                browser["Recently Closed"].push(tab);
                browser["Browser Logs"].push(command);
            }
        }
        
    }

    for (const key in browser) {
        if (key === "Browser Name") {
            console.log(browser[key]);
        } else {
            console.log(`${key}: ${browser[key].join(', ')}`)
        }
    }
}

// browserHistory(
//     {"Browser Name":"Google Chrome",
//     "Open Tabs":["Facebook","YouTube","Google Translate"],
//     "Recently Closed":["Yahoo","Gmail"],
//      "Browser Logs":["Open YouTube","Open Yahoo","Open Google Translate",
//      "Close Yahoo","Open Gmail","Close Gmail","Open Facebook"]}, 
//      ["Close Facebook", "Open StackOverFlow", "Open Google"]
// )

browserHistory(
    {"Browser Name":"Mozilla Firefox",

    "Open Tabs":["YouTube"],

    "Recently Closed":["Gmail", "Dropbox"],

    "Browser Logs":["Open Gmail",

    "Close Gmail", "Open Dropbox", "Open YouTube", "Close Dropbox"]},
    
["Open Wikipedia", "Clear History and Cache", "Open Twitter"]
)