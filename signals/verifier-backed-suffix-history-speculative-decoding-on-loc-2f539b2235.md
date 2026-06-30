# Verifier-backed suffix-history speculative decoding on local code completion

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `verifier-backed-suffix-history-speculative-decoding-on-loc-2f539b2235`
Run ID: `verifier-backed-suffix-history-speculative-decoding-on-loc-2f539b2235-20260613T031302964734+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Suffix-Tree Draft Beats N-gram Speculative Decoding on Local Code Completion: enoch://control-plane/projects/suffix-tree-draft-beats-n-gram-speculative-decoding-on-local-code-completion-04d25d055d9c/runs/suffix-tree-draft-beats-n-gram-speculative-decoding-on-local-code-completion-04d25d055d9c-20260613T024228473994+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/db5f0839bd52

## What looked useful

Verifier backing prevented wrong suffix-history commits and reconstructed all targets exactly, but accepted too few draft tokens for practical speedup. Main run achieved 1.0075x ideal speedup; best parameter-grid result achieved 1.0723x, still below the 1.10x Tier-1 threshold.

## Boundaries and scale limits

Only 80 local completion cases from a newly initialized project corpus; simple exact-reconstruction tokenizer; oracle verifier rather than live LLM forward passes; verifier-call speedup rather than measured wall-clock serving latency.

## Claim scope

Controlled small direct offline code-completion simulation over this local project workspace: verifier-backed suffix-history drafts preserved exact output but did not reach the predeclared 1.10x ideal verifier-call speedup threshold.

## Why it stopped

Early Tier-1 threshold failure: direct local oracle simulation supports exactness but not the required speedup, so the result is not paper-positive or worth deeper scale-only validation from this run.

## Recommended next action

Stop this follow-up as no-paper useful signal; only revisit with a larger real code corpus plus production tokenizer and live target-model verifier latency measurement.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/verifier-backed-suffix-history-speculative-decoding-on-loc-2f539b2235`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
