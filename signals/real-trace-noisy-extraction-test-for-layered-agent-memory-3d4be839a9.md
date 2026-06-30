# Real-trace noisy extraction test for layered agent memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-trace-noisy-extraction-test-for-layered-agent-memory-3d4be839a9`
Run ID: `real-trace-noisy-extraction-test-for-layered-agent-memory-3d4be839a9-20260629T030601159001+0000`

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

- Parent run decision: Layered Memory Stack: Working, Project, User, Operator on CPU: enoch://control-plane/projects/layered-memory-stack-working-project-user-operator-on-cpu-1cd7f9669349/runs/layered-memory-stack-working-project-user-operator-on-cpu-1cd7f9669349-20260629T024912055933+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ed224b707225

## What looked useful

Source/layer precedence removed stale-doctrine failures in the proxy: flat retrieval failed the stale replacement case while layered memory solved all cases. The predeclared layered-over-flat margin of 0.20 accuracy was not met.

## Boundaries and scale limits

No real trace corpus was available in the project. The benchmark used deterministic proxy cases, no LLM extraction, no large replay corpus, and no long-horizon memory compaction. Repetitions stress reproducibility rather than independent examples.

## Claim scope

In a six-case, hand-authored trace-like proxy benchmark with seven noisy extraction queries repeated 50 times, layered doctrine memory achieved 1.000 accuracy and beat transcript search by 0.429 accuracy, but beat flat retrieval by only 0.143 accuracy.

## Why it stopped

Proxy-only early test with no real traces available, and the predeclared layered-over-flat success threshold failed.

## Recommended next action

Stop this run as no-paper proxy evidence; next bounded action is to rerun the same harness on an anonymized real-trace corpus with at least 50 independent labeled extraction tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anonymized real-trace noisy extraction benchmark for layered agent memory
- Success threshold: Layered doctrine memory accuracy exceeds flat retrieval accuracy by at least 0.20 on at least 50 independent labeled real-trace queries, with no unresolved privacy leaks in artifacts.
- Stop condition: Stop if a real anonymized corpus cannot be supplied, if privacy review prevents durable artifacts, or if layered memory fails to beat flat retrieval by 0.20 accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-noisy-extraction-test-for-layered-agent-memory-3d4be839a9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
