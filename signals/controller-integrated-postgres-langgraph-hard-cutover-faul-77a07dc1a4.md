# Controller-integrated Postgres LangGraph hard-cutover fault injection

Status: `useful_signal`
Project ID: `controller-integrated-postgres-langgraph-hard-cutover-faul-77a07dc1a4`
Run ID: `controller-integrated-postgres-langgraph-hard-cutover-faul-77a07dc1a4-20260515T221452919565+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Controller-integrated Postgres LangGraph hard-cutover fault injection: internal_generated:controller-integrated-postgres-langgraph-hard-cutover-faul-77a07dc1a4

## What looked useful

PostgresSaver recovered graph completion in all local hard-cutover trials, but checkpointing alone did not provide exactly-once external side effects: duplicate side-effect attempts averaged 7.42 per 40-step Postgres trial under 8 SIGKILL cutovers, versus 0 in no-fault controls.

## Boundaries and scale limits

Does not test the full production Enoch controller, Postgres failover, host crashes, network partitions, concurrent controller ownership races, heterogeneous production traces, or long-duration multi-machine robustness.

## Claim scope

Local Docker/Postgres fault-injection harness using the actual installed LangGraph PostgresSaver: 12 fixed-seed fault-injected trials per mode, 40 graph steps per trial, 8 SIGKILL cutovers per trial, plus 12 no-fault controls per mode.

## Why it stopped

Moderate local direct evidence supports checkpoint-based completion recovery but falsifies the stronger exactly-once side-effect interpretation; the run is not Tier 4 paper-ready replication.

## Recommended next action

Stop this depth-4 follow-up as no-paper useful evidence; do not launch another deepen/retry follow-up from this lineage without a new controller decision.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/controller-integrated-postgres-langgraph-hard-cutover-faul-77a07dc1a4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
