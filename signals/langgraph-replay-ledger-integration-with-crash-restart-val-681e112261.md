# LangGraph replay ledger integration with crash-restart validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `langgraph-replay-ledger-integration-with-crash-restart-val-681e112261`
Run ID: `langgraph-replay-ledger-integration-with-crash-restart-val-681e112261-20260527T010923752279+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Deterministic Replay Ledger for 124M Agent Loops: enoch://control-plane/projects/deterministic-replay-ledger-for-124m-agent-loops-2e77703290f3/runs/deterministic-replay-ledger-for-124m-agent-loops-2e77703290f3-20260524T205636865355+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2d085e78b642

## What looked useful

Baseline crash/restart duplicated committed effects for extract and transform, while the replay-ledger variant exited 137 then restarted cleanly with exactly one committed effect for extract, transform, and load, plus replay_skip audit events for extract and transform.

## Boundaries and scale limits

Tested only local SQLite persistence, one thread_id per variant, one crash node, one restart, and deterministic node outputs. Not tested with concurrent workers, distributed LangGraph deployments, remote non-transactional side effects, network partitions, or longer agent workloads.

## Claim scope

In a deterministic three-node Python LangGraph 1.0.8 StateGraph using persistent SqliteSaver checkpoints, a SQLite replay ledger that atomically records node side effects and replayable outputs prevented duplicate external effects after a hard process crash before LangGraph checkpoint completion.

## Why it stopped

Tier 1 controlled small direct test succeeded and produced useful mechanism evidence, but it is not publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up with a crash-point matrix and concurrent thread_ids to test whether the ledger remains exactly-once under replay interleavings.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LangGraph replay ledger crash matrix with concurrent thread validation
- Success threshold: Across all after-ledger crash cases and concurrent thread_ids, the ledger variant has exactly one committed external effect per logical node execution, zero duplicate effects, successful restart completion, and audit events explaining every replay skip; baseline duplicates at least one replayed committed effect.
- Stop condition: Stop if any completed ledger row still allows a duplicate external effect on replay, if concurrent runs corrupt ledger state, or if the only remaining validation requires production-only private infrastructure.

## Evidence references

- Artifact root: `<local-path>/projects/langgraph-replay-ledger-integration-with-crash-restart-val-681e112261`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
