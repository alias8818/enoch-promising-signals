# Domain mix sweep for tiny pretraining: web/code/QA ratios on GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `domain-mix-sweep-for-tiny-pretraining-web-code-qa-ratios-on-gpt-2-small-70aa3784e265`
Run ID: `domain-mix-sweep-for-tiny-pretraining-web-code-qa-ratios-on-gpt-2-small-70aa3784e265-20260621T233832251088+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ef97128d263b

## What looked useful

Balanced 33/33/34 web/code/QA had the best two-seed mean macro loss (7.980). Web-heavy 60/25/15 had the best web loss (8.879). No-QA 50/50/0 had much worse QA loss (10.242) than balanced (9.463). QA-heavy did not beat balanced on QA, and code-heavy did not beat no-QA or balanced on code.

## Boundaries and scale limits

Only 120 optimizer steps per mixture, batch size 4, sequence length 128, 192 train sequences per mixture, 24 validation sequences per domain, and two random seeds. This does not validate full pretraining, downstream capability, long-context behavior, or large-corpus scaling.

## Claim scope

In a two-seed, 120-step GPT-2-small-from-scratch probe on Wikitext-2, CodeSearchNet Python, and SQuAD-formatted QA text, mixture ratios measurably changed early per-domain validation loss; balanced was best on macro loss, web-heavy was best on web loss, and removing QA sharply worsened QA loss.

## Why it stopped

No-paper closure: this is useful small-scale evidence, but the short run and tiny validation budget are insufficient for publication-grade or full-scale validation.

## Recommended next action

Run a bounded deepen follow-up with 1k-2k optimizer steps per mixture, at least 3 seeds, larger disjoint validation sets, and baseline-normalized per-domain loss deltas before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Longer normalized domain-mix confirmation for GPT-2-small web/code/QA pretraining
- Success threshold: Balanced mix has the best or statistically tied best normalized macro loss, web-heavy improves web normalized loss by at least 0.05 versus balanced without more than 0.10 normalized macro loss regression, and no-QA worsens QA normalized loss by at least 0.20 versus balanced across seed means.
- Stop condition: Stop if seed-to-seed variance exceeds the observed mixture effects, if no-QA no longer worsens QA loss, or if longer training collapses all mixture differences below 0.03 normalized loss.

## Evidence references

- Artifact root: `<local-path>/projects/domain-mix-sweep-for-tiny-pretraining-web-code-qa-ratios-on-gpt-2-small-70aa3784e265`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
