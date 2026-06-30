# KV-cache repetition-anchor speculation on real structured-output benchmarks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-repetition-anchor-speculation-on-real-structured-8cf124949b`
Run ID: `kv-cache-repetition-anchor-speculation-on-real-structured-8cf124949b-20260621T140924185475+0000`

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

- Parent run decision: Repetition-Anchored Self-Speculation for Structured Generation: enoch://control-plane/projects/repetition-anchored-self-speculation-for-structured-generation-f42e9eb10ea6/runs/repetition-anchored-self-speculation-for-structured-generation-f42e9eb10ea6-20260621T134922097317+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/eb7eeb8e14a3

## What looked useful

Canonical structured outputs showed online-global anchor-8 candidate coverage of 74.02%, 65.18%, 66.22%, and 93.39% across data table analysis, financial entities, insurance claims, and PII extraction, versus input-text controls of 6.13%, 5.32%, 1.85%, and 0.00%. Within-sequence canonical coverage was only 11.62%, 0.01%, 5.50%, and 0.00%.

## Boundaries and scale limits

No transformer forward pass, KV materialization, verifier, constrained decoder, scheduler, or live serving stack was measured. Within-sequence-only coverage was weak on three of four datasets, so the signal mainly applies to cross-request/template reuse for repeated schemas.

## Claim scope

On four Cleanlab real structured-output benchmark datasets, GPT-2-tokenized ground-truth structured outputs have high exact repeated-span candidate coverage for an online cross-example/template-cache repetition-anchor simulator at anchor length 8 and minimum accepted span 8. The claim is limited to candidate availability, not measured serving speedup.

## Why it stopped

Tier 1 direct token-level mechanism test passed for cross-example/template candidate coverage, but actual KV-cache speedup and within-request benefit were not demonstrated.

## Recommended next action

Stop this run as no-paper useful signal; next run should build a local small-model serving prototype that measures net tokens/sec and overhead for cross-request/template repetition-anchor speculation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live small-model serving test for cross-request structured-output repetition-anchor speculation
- Success threshold: At least 10% net tokens/sec improvement on two repeated-schema datasets with identical final outputs and less than 10% memory overhead, while showing no claimed gain on the schema-varied control.
- Stop condition: Stop if accepted spans remain high but lookup plus verification overhead erases net throughput gains, or if output equality/correctness cannot be preserved.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-repetition-anchor-speculation-on-real-structured-8cf124949b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
