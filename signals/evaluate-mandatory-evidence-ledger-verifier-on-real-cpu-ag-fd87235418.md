# Evaluate mandatory evidence-ledger verifier on real CPU-agent transcripts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evaluate-mandatory-evidence-ledger-verifier-on-real-cpu-ag-fd87235418`
Run ID: `evaluate-mandatory-evidence-ledger-verifier-on-real-cpu-ag-fd87235418-20260619T181928115346+0000`

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

- Parent run decision: Mandatory evidence-ledger actions for CPU small agents: enoch://control-plane/projects/mandatory-evidence-ledger-actions-for-cpu-small-agents-b462091a183a/runs/mandatory-evidence-ledger-actions-for-cpu-small-agents-b462091a183a-20260619T180512138063+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e4e06b2a7886

## What looked useful

The verifier mechanism is viable for enforcing non-empty claims, mandatory evidence_refs, reference integrity, duplicate evidence ID rejection, and optional transcript line anchors on real CPU-agent JSONL logs.

## Boundaries and scale limits

Only one local in-project Codex JSONL transcript was available; negative cases were controlled mutations, so this does not establish broad naturalistic false accept/reject rates or paper readiness.

## Claim scope

Tier 1 controlled small direct test: a dependency-free mandatory evidence-ledger verifier accepted one real local CPU-agent transcript ledger with line-anchored evidence and rejected five controlled invalid ledgers.

## Why it stopped

Tier 1 mechanism support produced useful no-paper evidence; the available local corpus is too small and mutation-based for publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up on at least 20 independent real CPU-agent transcripts with manually labeled valid/invalid ledgers before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Measure verifier false accept and false reject rates on independent CPU-agent transcript ledgers
- Success threshold: False accept rate <= 5% and false reject rate <= 10% on the labeled transcript-ledger corpus, with every evidence item anchored to an existing transcript line.
- Stop condition: Stop if any unsupported claim with missing, dangling, duplicate, or bad-anchor evidence is accepted, or if valid transcript-anchored ledgers exceed a 10% false reject rate after the first 20 cases.

## Evidence references

- Artifact root: `<local-path>/projects/evaluate-mandatory-evidence-ledger-verifier-on-real-cpu-ag-fd87235418`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
