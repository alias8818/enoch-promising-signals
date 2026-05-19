# Hybrid Adam with spectral second-moment compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hybrid-adam-with-spectral-second-moment-compression-8164ad3e08`
Run ID: `hybrid-adam-with-spectral-second-moment-compression-8164ad3e08-20260518T085307421718+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/70f36d7b4575

## What looked useful

Rank 8 met the Tier 1 threshold: low-rank task median validation loss ratio 1.042x vs Adam at 0.594x optimizer-state elements. Rank 4 was too compressed for the low-rank task at 1.089x Adam loss, while dense-target regression did not falsify the mechanism and showed lower validation loss than Adam in this small setup.

## Boundaries and scale limits

No transformer, GPT-2-class, language-model perplexity, long-run schedule, mixed-precision, distributed, or wall-clock overhead validation was performed. The implementation reconstructs and recompresses with SVD each step and was evaluated only on small single-matrix regression tasks.

## Claim scope

On small controlled 96x96 linear-regression matrix-parameter tasks, a hybrid spectral Adam second-moment state with rank 8 plus row/column residuals reduced optimizer-state elements to 59.4% of dense Adam while staying within 1.05x Adam median validation loss on the low-rank task across 3 seeds.

## Why it stopped

Tier 1 direct controlled test produced useful mechanism support but not publication-grade evidence; rank sensitivity and SVD overhead remain unresolved.

## Recommended next action

Run a bounded small-transformer or GPT-2-small-class confirmation comparing dense Adam to rank-8 and rank-16 hybrid spectral Adam on validation perplexity, optimizer-state memory, and measured step-time overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small Transformer Confirmation for Hybrid Spectral Adam
- Success threshold: At least one compressed rank achieves <=70% dense-Adam optimizer-state memory, final validation perplexity <=1.02x dense Adam, and step-time overhead <=25% in the bounded transformer run.
- Stop condition: Stop if all compressed ranks exceed 1.02x dense Adam validation perplexity or exceed 25% step-time overhead after the planned bounded run.

## Evidence references

- Artifact root: `<local-path>/projects/hybrid-adam-with-spectral-second-moment-compression-8164ad3e08`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
