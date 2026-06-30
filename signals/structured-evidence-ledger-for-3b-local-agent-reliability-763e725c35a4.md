# Structured evidence ledger for 3B local agent reliability

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `structured-evidence-ledger-for-3b-local-agent-reliability-763e725c35a4`
Run ID: `structured-evidence-ledger-for-3b-local-agent-reliability-763e725c35a4-20260607T150345333831+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/14ba056c8bbc

## What looked useful

The benchmark harness is reproducible and exposed a severe local-stack failure: the tested Phi-4-mini GGUF/runtime could not produce valid JSON on 20 paired evidence tasks or on trivial JSON sanity prompts. Ledger prompting did not recover reliability in the medium run.

## Boundaries and scale limits

Synthetic short-context tasks only; one 3.84B GGUF model and one llama.cpp server build; no real tool-use agent, no long-horizon memory, no retrieval workflow, and no verified alternate 3B runtime because the Qwen2.5-3B retry download made no progress.

## Claim scope

On a deterministic 20-task synthetic evidence benchmark using Phi-4-mini-instruct-Q4_K_M.gguf served by llama.cpp on GB10, structured evidence ledger prompting did not improve local 3B-class agent reliability; both baseline and ledger conditions achieved 0.0 answer, evidence, joint, and JSON-validity rates.

## Why it stopped

Proxy medium confirmation failed: both conditions scored 0/20 valid JSON and 0/20 exact answer/evidence success, and trivial JSON sanity checks also failed for the tested Phi runtime.

## Recommended next action

Stop this run as an early proxy/local-stack negative; retry the harness only after verifying a 3B-class model/runtime can pass trivial JSON sanity checks.

## Follow-up

- Recommended: `true`
- Type: `retry`
- Title: Retry structured evidence ledger benchmark on a sanity-checked 3B local runtime
- Success threshold: Ledger condition improves joint accuracy by at least 10 percentage points over baseline while maintaining JSON validity at or above 90%.
- Stop condition: Stop early if either condition has JSON validity below 50% after the first 20 paired tasks, because that indicates the runtime is not suitable for testing the ledger mechanism.

## Evidence references

- Artifact root: `<local-path>/projects/structured-evidence-ledger-for-3b-local-agent-reliability-763e725c35a4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
