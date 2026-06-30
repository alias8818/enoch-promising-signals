# Evidence-Ledger Sub-Claim Audit for Local Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-sub-claim-audit-for-local-agents-d0f677bd906e`
Run ID: `evidence-ledger-sub-claim-audit-for-local-agents-d0f677bd906e-20260613T225158348459+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ffdbb53a6b0a

## What looked useful

Claim-level evidence-ledger auditing missed 12/12 mixed composite unsupported cases, while sub-claim all-required auditing caught 12/12, improving overall unsupported-claim recall from 0.667 to 1.000 on the benchmark.

## Boundaries and scale limits

Proxy-only structured triples; no natural-language decomposition, retrieval, citation selection, paraphrase/contradiction handling, or real local-agent transcript diversity was tested.

## Claim scope

On 48 structured local evidence-ledger cases with pre-decomposed composite claims, requiring every atomic sub-claim to be supported caught mixed unsupported conclusions that a permissive claim-level any-hit audit missed.

## Why it stopped

Proxy structured evidence supports the mechanism but is not direct/full validation of deployed local agents or LLM sub-claim extraction.

## Recommended next action

Run a bounded deepen follow-up on natural-language local-agent transcripts with human-labeled atomic sub-claims and evidence citations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language sub-claim audit on local-agent evidence ledgers
- Success threshold: At least +15 percentage points unsupported-subclaim recall versus claim-level audit with precision no more than 5 percentage points lower on 100 or more labeled natural-language claims.
- Stop condition: Stop if sub-claim auditing improves recall by less than 5 percentage points, or if precision drops by more than 10 percentage points, after the labeled benchmark reaches 100 claims.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-sub-claim-audit-for-local-agents-d0f677bd906e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
