/*

    api:

        list    // lists items for this dir
        list -g // lists all lists
        add     // adds note to current dirs notes. if no list, it creates it and prompts for a list name.
        nix     // removes dir 

    data structure:

        list of objects for each list 

*/


const app = module.exports = exports = {

    currentDirectory: getCwd(),
    lists: [],
    makeList, 
    deleteList,
    editTask,
    addTask

};

const getCwd = () => {
    return process.cwd;
}

const getList = () => {
    // this will determine appropriate list if dir doesn't match existing lists
    return getCwd();
};

const commander = require('commander');

commander
    .command('list')
    .option('-g, --global')
    .action( listAll(app.lists) );

commander
    .command('add')
    .action( addTask(app.lists) );


commander.parse(process.argv);

const listAll = (options) => {
    if (options.global) {
        listAllLists(app.lists);
    } else {
        listAllTasks(getList())
    }
};

const listAllTasks = (list) => {
    list.tasks.forEach(task => console.log(task.title)); 
}

const listAllLists = (lists) => {
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
