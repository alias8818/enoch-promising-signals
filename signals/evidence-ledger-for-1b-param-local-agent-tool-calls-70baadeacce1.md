# Evidence Ledger for 1B-Param Local Agent Tool Calls

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-for-1b-param-local-agent-tool-calls-70baadeacce1`
Run ID: `evidence-ledger-for-1b-param-local-agent-tool-calls-70baadeacce1-20260529T005913264810+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bc97cb3bdc1b

## What looked useful

The ledger substrate is technically viable for off-context audit logging: 10,000 events built at 104,376 events/second, verification under tamper cases took 32.07 ms median, and 60/60 synthetic tamper trials were detected. The useful result is the bounded mechanism and overhead profile, not a validated improvement to 1B-agent behavior.

## Boundaries and scale limits

This did not run a real 1B-parameter model, real tool outputs, adversarial prompts, long-context agent trajectories, or human/private tasks. Storage overhead was 15.46x over a plain claim-only text baseline, and coordinated removal of both ledger tail and downstream claims requires an external root hash, event-count checkpoint, or run manifest to detect.

## Claim scope

In a deterministic 10,000-event synthetic tool-call benchmark, a compact hash-chained evidence ledger with claim-to-output-hash bindings detected all tested altered, deleted, reordered, fabricated-reference, wrong-hash, and tail-truncation attacks when the claim set remained available, while using one CPU process and under 44 MB RSS.

## Why it stopped

Closed as no-paper useful signal because this was a synthetic ledger-substrate validation, not direct full evidence for 1B-parameter local agent tool-call behavior.

## Recommended next action

Run a bounded deepen follow-up that integrates this ledger into an actual 1B-class local agent tool-use harness and measures citation correctness, audit recovery, context overhead, and task success against a no-ledger/plain-transcript control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Integrate Evidence Ledger Into a 1B-Class Local Tool-Use Agent
- Success threshold: Across at least 100 real tool-use episodes, ledger mode should detect at least 95% of injected evidence faults, keep task success within 5 percentage points of the best control, and keep median added latency below 10% excluding model generation time.
- Stop condition: Stop if ledger mode fails to detect at least 90% of injected evidence faults, causes more than a 10 percentage point task-success drop, or prompt/context overhead makes more than 20% of episodes exceed the model context window.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-1b-param-local-agent-tool-calls-70baadeacce1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
