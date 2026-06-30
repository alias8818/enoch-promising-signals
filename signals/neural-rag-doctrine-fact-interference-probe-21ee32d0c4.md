# Neural RAG Doctrine-Fact Interference Probe

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `neural-rag-doctrine-fact-interference-probe-21ee32d0c4`
Run ID: `neural-rag-doctrine-fact-interference-probe-21ee32d0c4-20260613T075030143382+0000`

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

- Parent run decision: Memory Architecture: Operator Doctrine vs Fact Storage: enoch://control-plane/projects/memory-architecture-operator-doctrine-vs-fact-storage-41a477a1051c/runs/memory-architecture-operator-doctrine-vs-fact-storage-41a477a1051c-20260613T073430512362+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/6db3840ff63f

## What looked useful

Conflicting doctrine passages reduced forced-choice fact accuracy from 1.000 in fact-only and neutral controls to 0.861 mean conflict accuracy across three seeds, but conflicting doctrine labels were selected only 0.118 of conflict trials, below the predeclared 0.25 mechanism threshold.

## Boundaries and scale limits

Synthetic corpus only; simulated retrieval by prompt ordering; one small instruction-tuned model; no production retriever, real doctrine corpus, larger LLM, or multi-model robustness validation.

## Claim scope

Small controlled FLAN-T5-small RAG-style QA test with synthetic case IDs, fact records, neutral doctrine memos, and conflicting doctrine memos under deterministic generation and forced-choice scoring.

## Why it stopped

Tier 1 direct test produced a stable but sub-threshold useful signal: accuracy dropped about 14 percentage points under conflict, but doctrine-label adoption stayed around 12%, so mechanism support is mixed and not paper-positive.

## Recommended next action

Run a bounded deepen follow-up with two or three stronger instruction models plus a real lightweight retriever and the same fact/neutral/conflict controls before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-model retrieved-context doctrine interference confirmation
- Success threshold: Across at least two models, conflict contexts reduce fact-answer accuracy by >=0.20 versus neutral/fact-only controls and select the conflicting doctrine label in >=0.25 of conflict trials.
- Stop condition: Stop as negative if fact-only and neutral controls are >=0.70 accurate but conflict accuracy drops <0.10 or doctrine-choice rate remains <0.15 across the tested models.

## Evidence references

- Artifact root: `<local-path>/projects/neural-rag-doctrine-fact-interference-probe-21ee32d0c4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
