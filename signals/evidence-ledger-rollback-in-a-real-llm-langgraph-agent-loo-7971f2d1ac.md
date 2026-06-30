# Evidence-ledger rollback in a real LLM LangGraph agent loop

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-rollback-in-a-real-llm-langgraph-agent-loo-7971f2d1ac`
Run ID: `evidence-ledger-rollback-in-a-real-llm-langgraph-agent-loo-7971f2d1ac-20260524T203646329277+0000`

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

- Parent run decision: Evidence-ledger agent rollback on CPU: enoch://control-plane/projects/evidence-ledger-agent-rollback-on-cpu-ed2c60140495/runs/evidence-ledger-agent-rollback-on-cpu-ed2c60140495-20260524T194945257712+0000
- Parent run decision: Evidence-ledger rollback in a real tool-using LLM agent harness: enoch://control-plane/projects/evidence-ledger-rollback-in-a-real-tool-using-llm-agent-ha-200d93d7b9/runs/evidence-ledger-rollback-in-a-real-tool-using-llm-agent-ha-200d93d7b9-20260524T202539682932+0000

## What looked useful

Rollback removed three invalidated stale claims per case. In the Qwen 0.5B fixed-seed run, rollback achieved 1.000 accuracy and 0.000 stale-use versus append-only 0.867 accuracy/0.133 stale-use and verifier-without-rollback 0.733 accuracy/0.267 stale-use. The deterministic mechanism run over 100 cases showed the same direction with a larger effect.

## Boundaries and scale limits

Synthetic task family; 15 real-model cases due CPU cost; candidate-scoring answerer rather than fully open-ended chat/tool planning; one instruction-tuned local model plus one non-instruction negative smoke; no production traces, persistence/resume stress test, or larger multi-model benchmark.

## Claim scope

In a controlled synthetic stale-evidence task, a real LangGraph agent loop with physical evidence-ledger rollback reduced stale-evidence use and improved final color-answer accuracy versus append-only and verifier-without-rollback controls. The strongest real-model evidence is Qwen/Qwen2.5-0.5B-Instruct offline candidate scoring over 15 fixed-seed cases.

## Why it stopped

No-paper useful signal: bounded fixed-seed baseline and ablation support the rollback mechanism, but the real-model sample is small and synthetic, so evidence is below publication readiness.

## Recommended next action

Run a larger bounded real-LLM deepen test with at least 100 cases, open-ended chat/tool-call answering, persistence/resume checks, and two model families before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Larger open-ended real-LLM validation of LangGraph evidence-ledger rollback
- Success threshold: Rollback improves stale-evidence use by at least 20 percentage points against both controls, does not reduce completion by more than 5 percentage points, and has invalid rollback rate under 2%.
- Stop condition: Stop if two capable instruction-tuned models show less than 5 percentage points stale-use reduction versus verifier-without-rollback or if invalid rollback exceeds 5%.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-rollback-in-a-real-llm-langgraph-agent-loo-7971f2d1ac`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
