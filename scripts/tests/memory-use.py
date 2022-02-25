"""Memory use and profiles."""

# WIP
# TODO - for future edit and use, not currently used, need refactor

import linecache
import platform
import tracemalloc

import pytest

# Set test discovery path
start_dir = "test"

# Set module to test
test_module = "WIP"


def display_top(snapshot, key_type="lineno", limit=5):
    """Display top values from memory analysis."""
    snapshot = snapshot.filter_traces(
        (
            tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
            tracemalloc.Filter(False, "<unknown>"),
        )
    )
    top_stats = snapshot.statistics(key_type)

    print("Top %s lines" % limit)
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        print(
            "#%s: %s:%s: %.1f KiB"
            % (index, frame.filename, frame.lineno, stat.size / 1024)
        )
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print("    %s" % line)

    other = top_stats[limit:]
    if other:
        size = sum(stat.size for stat in other)
        print("%s other: %.1f KiB" % (len(other), size / 1024))
    total = sum(stat.size for stat in top_stats)
    print("Total allocated size: %.1f KiB" % (total / 1024))


# Confirm python
print()
print(f"Python: {platform.python_version_tuple()}")
print()

# Start tracing memory allocations
tracemalloc.start()

# Run tests to cause memory capture
retcode = pytest.main(["--tb=long", "-vrA", start_dir])

# Capture memory allocations stats
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")
trace_stats = snapshot.statistics("traceback")

print("[ Top 5 ]")
for stat in top_stats[:5]:
    print(stat)

print("------------------------------------------------------")
print()

display_top(snapshot)

print("------------------------------------------------------")
print()

# pick the biggest memory block
stat = trace_stats[0]
print("%s memory blocks: %.1f KiB" % (stat.count, stat.size / 1024))
for line in stat.traceback.format():
    print(line)

print("")
