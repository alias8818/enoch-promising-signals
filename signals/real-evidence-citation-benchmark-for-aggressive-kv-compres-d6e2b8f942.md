# Real Evidence-Citation Benchmark for Aggressive KV Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-evidence-citation-benchmark-for-aggressive-kv-compres-d6e2b8f942`
Run ID: `real-evidence-citation-benchmark-for-aggressive-kv-compres-d6e2b8f942-20260629T121159515596+0000`

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

- Parent run decision: Does Aggressive KV Compression Break Agent Evidence Citation?: enoch://control-plane/projects/does-aggressive-kv-compression-break-agent-evidence-citation-cdd5d70df45b/runs/does-aggressive-kv-compression-break-agent-evidence-citation-cdd5d70df45b-20260629T115600921927+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/44e2a0250434

## What looked useful

Evidence-aware retention is the dominant diagnostic in this bounded setup: head/tail policies retain gold evidence about 27% of the time and score about 0.22 F1, whereas query-overlap retains gold evidence about 96% of the time and scores about 0.83 F1, near the full-context 0.82 F1 baseline.

## Boundaries and scale limits

Proxy context-retention benchmark only; no real KV-cache compression kernel, no long-context citation-generating LLM, synthetic distractor mixtures, and only 3 seeds x 64 examples.

## Claim scope

On a small SQuAD-derived evidence-citation proxy benchmark using an extractive QA model, aggressive position-only retention at about 23% of tokens drops most gold evidence and loses about 0.60 F1 versus full context, while a simple query-aware retention policy preserves about 96% of gold evidence and matches full-context F1.

## Why it stopped

Proxy-scale evidence is useful but insufficient for a paper or a direct claim about real serving-time KV compression.

## Recommended next action

Stop this run as a no-paper useful signal; next, run a bounded direct test with an actual KV-cache compression implementation on a citation-generating long-context model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct KV-Compressed Citation QA on a Small Long-Context Generator
- Success threshold: At a fixed compression ratio near 25%, evidence-aware KV retention recovers at least 80% of full-context citation-supported answer accuracy and beats position-only retention by at least 20 percentage points in citation support.
- Stop condition: Stop if real KV compression cannot be instrumented locally or if full-context generation is too weak to reach 50% citation-supported answer accuracy on the selected benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/real-evidence-citation-benchmark-for-aggressive-kv-compres-d6e2b8f942`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
