const commander = require('commander');
const app = module.exports = exports = {

    currentDirectory: getCwd(),
    lists: [],
    makeList, 
    deleteList,
    editTask,
    addTask

};

commander
    .command('list')
    .option('-g, --global')
    .action( listAll(app.lists) );

commander
    .command('add')
    .action( addTask(app.lists) );


commander.parse(process.argv);

function getCwd() {
    return process.cwd;
}

function getList() {
    // this will determine appropriate list if dir doesn't match existing lists
    return getCwd();
};


function listAll(options) {
    if (options.global) {
        listAllLists(app.lists);
    } else {
        listAllTasks(app.lists)
    }
};

function listAllTasks(list) {
    list[0].tasks.forEach(task => console.log(task.title)); 
}

function listAllLists(lists) {
    lists.forEach(list => console.log(list.listName));
}


function makeTask(title, description, reminderInterval) {

    return {

        title,
        description,
        reminderInterval,

    };

}

function makeList(directory, listName, items=[]) {

    return {

        directory,
        listName,
        items,

    };

};

function addList(lists, listName) {

    if (lists.listName) return error('ADD_ERROR:LIST_EXISTS');

    let directory = process.cwd;
    let newList = makeList(directory, listName);

    lists[listName].push(newList);

}

function deleteList(listName) {

    lists.listName = null;

}

function editTask(listName, index, update) {
    lists[listName].tasks[index] = update;
}

function addTask(listName, taskIndex, [title, description, reminderInterval] = taskDetails) {

    let task = makeTask(title, description, reminderInterval);
    lists[listName].tasks[taskIndex].push(task);

}
